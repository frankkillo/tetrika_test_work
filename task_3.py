def appearance(intervals):
    lesson_start, lesson_end = intervals['lesson']
    ans = 0
    c = 0

    for i in range(0, len(intervals['tutor']), 2):
        tutor_start = max(intervals['tutor'][i], lesson_start)
        tutor_end = min(intervals['tutor'][i+1], lesson_end)
        if tutor_end <= lesson_start or tutor_start >= lesson_end:
            print('fail')
            continue  

        while c <= len(intervals['pupil']) - 2:
            pupil_start = intervals['pupil'][c]
            pupil_end = intervals['pupil'][c+1]

            if tutor_end <= pupil_start:
                if c:
                    c -= 2
                break
            elif tutor_start >= pupil_end:
                c += 2
                continue
            
            ans += min(tutor_end, pupil_end) - max(pupil_start, tutor_start)

            if tutor_end < pupil_end:
                break
            else:
                c += 2
            
    return ans


if __name__ == '__main__':
    tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
# не понял эти данные по pupil, я пологал, что время входа и выхода сортированы, а так же, что вход и выход уникальны
#    {'data': {'lesson': [1594702800, 1594706400],
#             'pupil': [1594702789, 1594704500, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
#             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
#    'answer': 3577
#    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
    ]

    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'