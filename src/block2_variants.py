import random

random.seed(42)


def run_b2_v3(n=100000):
    print("===== БЛОК 2 - Варіант 3 =====")
    th_a = 0.50
    th_b = 0.375
    th_ab = 0.0
    th_aub = 0.875
    th_cond = 0.50 / 0.875

    p1 = 0.50
    p2 = 0.75

    ca, cb, cab, caub = 0, 0, 0, 0

    for _ in range(n):
        a = random.random() < p1
        b = False if a else (random.random() < p2)

        if a:
            ca += 1
        if b:
            cb += 1
        if a and b:
            cab += 1
        if a or b:
            caub += 1

    wa = ca / n
    wb = cb / n
    wab = cab / n
    waub = caub / n
    w_cond = ca / caub if caub > 0 else 0

    print(f"Кількість симуляцій: {n}")
    print(
        f"Подія A (1-ша успішна) | Статистична: {wa:.4f} | Теоретична: {th_a:.4f} | Похибка: {abs(wa - th_a):.4f}"
    )
    print(
        f"Подія B (2-га успішна) | Статистична: {wb:.4f} | Теоретична: {th_b:.4f} | Похибка: {abs(wb - th_b):.4f}"
    )
    print(
        f"Перетин A ∩ B          | Статистична: {wab:.4f} | Теоретична: {th_ab:.4f} | Похибка: {abs(wab - th_ab):.4f}"
    )
    print(
        f"Об'єднання A U B       | Статистична: {waub:.4f} | Теоретична: {th_aub:.4f} | Похибка: {abs(waub - th_aub):.4f}"
    )
    print(
        f"Умовна P(A|A U B)      | Статистична: {w_cond:.4f} | Теоретична: {th_cond:.4f} | Похибка: {abs(w_cond - th_cond):.4f}"
    )
    print(
        f"Перевірка ПР ТЙ P(A U B) = P(A) + P(B) - P(A ∩ B): {waub:.4f} ≈ {wa + wb - wab:.4f}\n"
    )


def run_b4_v3(n=100000):
    print("===== БЛОК 4 - Варіант 3 =====")
    p_bld = 0.90
    p_tst = 0.85
    p_dep = 0.95
    p_th = p_bld * p_tst * p_dep

    ok = 0
    for _ in range(n):
        if random.random() < p_bld:
            if random.random() < p_tst:
                if random.random() < p_dep:
                    ok += 1

    w_ok = ok / n
    err = abs(w_ok - p_th)

    print(f"Змодельовано запусків CI/CD: {n}")
    print(f"Знайдена статистична частота успіху: {w_ok:.5f}")
    print(f"Теоретична ймовірність за умовою:    {p_th:.5f}")
    print(f"Абсолютна похибка результату:        {err:.5f}\n")


if __name__ == "__main__":
    run_b2_v3(n=100000)
    run_b4_v3(n=100000)