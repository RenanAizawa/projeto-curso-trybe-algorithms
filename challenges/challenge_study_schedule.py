def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    count_target = 0
    try: 
        for dupla in permanence_period:
            num1 = int(dupla[0])
            num2 = int(dupla[1])
            time = int(target_time)
            if num1 == time or num2 == time:
                count_target += 1
    except Exception:
        return None
    return count_target
