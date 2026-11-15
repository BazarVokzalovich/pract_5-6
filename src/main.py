import os
import random
import matplotlib.pyplot as plt

random.seed(42)
os.makedirs("graphics", exist_ok=True)


def run_b1():
    print("===== БЛОК 1 =====")
    p_b = 0.30
    p_ab = 0.70
    p_anb = 0.10
    p_ba_th = 0.75
    n_vals = [100, 1000, 10000, 100000, 1000000]

    err_list = []

    for n in n_vals:
        ma, mb, mab = 0, 0, 0
        for _ in range(n):
            b = random.random() < p_b
            a = (random.random() < p_ab) if b else (random.random() < p_anb)
            if a:
                ma += 1
            if b:
                mb += 1
            if a and b:
                mab += 1

        wa = ma / n
        wb = mb / n
        wab = mab / n
        wba = mab / ma if ma > 0 else 0
        err = abs(wba - p_ba_th)

        err_list.append(err)
        print(
            f"N = {n:7d} | W(A)={wa:.4f} | W(B)={wb:.4f} | W(A∩B)={wab:.4f} | W(B|A)={wba:.4f} | Похибка={err:.4f}"
        )

    plt.figure(figsize=(10, 5))
    plt.plot(
        n_vals, err_list, marker="o", color="r", label="Абсолютна похибка |W(B|A) - 0.75|"
    )
    plt.xscale("log")
    plt.xlabel("Кількість запитів N (лог. шкала)")
    plt.ylabel("Абсолютна похибка")
    plt.title("Блок 1: Збіжність похибки оцінки P(B|A) до 0")
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig("graphics/block1_convergence.png")
    plt.close()

def run_b3():
    print("\n===== БЛОК 3 =====")
    p1, p2, p3, p4, p5 = 0.98, 0.90, 0.90, 0.95, 0.95
    p_th = p1 * (1 - (1 - p2) * (1 - p3)) * (1 - (1 - p4) * (1 - p5))
    n_vals = [100, 1000, 10000, 100000, 1000000]

    w_list = []

    for n in n_vals:
        ok = 0
        for _ in range(n):
            lb = random.random() < p1
            w1 = random.random() < p2
            w2 = random.random() < p3
            d1 = random.random() < p4
            d2 = random.random() < p5
            if lb and (w1 or w2) and (d1 or d2):
                ok += 1

        w = ok / n
        w_list.append(w)
        print(
            f"N = {n:7d} | Оцінка W_sys = {w:.5f} | Теорія P_sys = {p_th:.5f} | Похибка = {abs(w - p_th):.5f}"
        )

    plt.figure(figsize=(10, 5))
    plt.axhline(
        y=p_th,
        color="g",
        linestyle="--",
        label=f"Теоретична надійність P_sys ({p_th:.4f})",
    )
    plt.plot(
        n_vals, w_list, marker="s", color="b", label="Оцінка Монте-Карло W_sys"
    )
    plt.xscale("log")
    plt.xlabel("Кількість випробувань N (лог. шкала)")
    plt.ylabel("Надійність системи")
    plt.title("Блок 3: Збіжність оцінки надійності системи до P_sys")
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig("graphics/simulation_results.png")
    plt.close()
    print("\n[УСПІХ]: Блоки 1 та 3 виконано, графіки збережено в 'graphics/'!")


if __name__ == "__main__":
    run_b1()
    run_b3()
