def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    count_target = 0
    try:
        for dupla in permanence_period:
            if dupla[0] <= target_time <= dupla[1]:
                count_target += 1
    except (TypeError, ValueError):
        return None
    return count_target
