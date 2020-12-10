from typing import List, Optional

import pronouncing


def stresses_for_words(s: str) -> Optional[str]:
    all_stresses = []
    wds = s.split()
    for wd in wds:
        wd_stresses = pronouncing.stresses_for_word(wd)
        if not wd_stresses:
            # if any word is unpronounceable , bail
            return None

        wd_stresses = two_stress_levels(wd_stresses)
        print('stresses for {}:\n\t{}'.format(wd, wd_stresses))
        all_stresses.extend(wd_stresses)

    # don't differentiate between primary and secondary stress
    return all_concats(all_stresses)

# def stresses_for_words(s: str) -> Optional[str]:
#     txt = prosodic.Text(s)
#     stresses = ''.join([wd.stress for wd in txt.words()])
#     if '?' in stresses:
#         return None
#     return stresses.replace('P', '1').replace('S', '1').replace('U', '0')


def two_stress_levels(stresses: List[str]) -> List[str]:
    for i, stress in enumerate(stresses):
        stresses[i] = stress.replace('2', '1')
    return list(set(stresses))


def any_is_trochaic_tetrameter(s: str) -> bool:
    stresses = stresses_for_words(s)
    print('HI THERE')
    print(stresses)
    for stress in stresses:
        if is_trochaic_tetrameter(stress):
            return True
    return False


def is_trochaic_tetrameter(stresses: str) -> bool:
    if len(stresses) != 8:
        return False

    for i, stress in enumerate(stresses):
        if i % 2 == 0:
            if stress == '0':
                # unstressed even syllable
                return False
    return True


def all_concats(inp, so_far=''):
    result = set()
    if len(inp) == 0:
        return {so_far}
    for val in inp[0]:
        result.update(all_concats(inp[1:], so_far=so_far+val))
    return result