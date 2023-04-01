# Samy Sabir 261119166

import doctest, musicalbeeps, note


def has_limit_octave(notes_list, min_octave, max_octave):
    """ () -> bool
    Checks a lits of Note objects for any object
    with octave equal to 1 or 7 (OCTAVE_MIN and OCTAVE_MAX)
    Returns True if so
    Otherwise returns False

    >>> happy_birthday = Melody("birthday.txt")
    >>> notes_list = happy_birthday.notes
    >>> has_limit_octave(notes_list, 1, 7)
    False

    >>> happy_birthday = Melody("birthday.txt")
    >>> notes_list = happy_birthday.notes
    >>> has_limit_octave(notes_list, 1, 4)
    True

    >>> happy_birthday = Melody("birthday.txt")
    >>> notes_list = happy_birthday.notes
    >>> has_limit_octave(notes_list, 3, 5)
    True
    """

    for i in notes_list:
        if i.pitch != 'R':
            if i.octave == min_octave or i.octave == max_octave:
                return True

    return False


class Melody:
    """ Stores information about a melody of many notes.

    Instance attributes:
    *title = str
    *author = str
    *notes = list<Note>
    """

    def __init__(self, filename):
        """ (str) -> NoneType
        Creates an object of type Melody
        and its instance attributes

        >>> happy_birthday = Melody("birthday.txt")
        >>> len(happy_birthday.notes)
        25
        >>> print(happy_birthday.notes[5])
        1.0 F 4 sharp

        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> len(hot_cross_buns.notes)
        17
        >>> print(hot_cross_buns.notes[14])
        0.5 B 4 natural

        >>> twinkle = Melody("twinkle.txt")
        >>> len(twinkle.notes)
        42
        >>> print(twinkle.notes[28])
        0.5 C 4 natural
        """

        fobj = open(filename, 'r')
        file_content = fobj.read()
        lines = file_content.split('\n')
        self.title = lines[0]
        self.author = lines[1]

        temp_notes = []
        lines = lines[2:]
        i = 0
        counter = 0
        first_time = False

        while i < len(lines):
            if 'true' in lines[i]:
                if not first_time:
                    line_index = i
                counter += 1
                first_time = True
                if counter == 0:
                    first_time = False

            e = lines[i].strip().split(' ')
            if 'R' in e:
                temp_notes.append(note.Note(float(e[0]), e[1]))
            else:
                temp_notes.append(note.Note(float(e[0]), e[1], int(e[2]), e[3].lower()))

            if counter > 1:
                counter = -2
                i = line_index
            else:
                i += 1

        self.notes = temp_notes
        fobj.close()

    def play(self, player=musicalbeeps.Player()):
        """ (Player) -> NoneType
        Takes a music player object as input
        Calls the play method from the Note class
        on each Note object of the notes instance attribute in order
        """

        for i in self.notes:
            i.play(player)

    def get_total_duration(self):
        """ () -> float
        Return the total duration of the song as a float

        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.get_total_duration()
        13.0

        >>> twinkle = Melody("twinkle.txt")
        >>> twinkle.get_total_duration()
        24.5

        >>> fur_elise = Melody("fur_elise.txt")
        >>> fur_elise.get_total_duration()
        25.799999999999944
        """

        total = 0
        for i in self.notes:
            total += i.duration

        return total

    def lower_octave(self):
        """ () -> bool
        Reduces the octave of all notes in the song by 1
        and returns True
        If one octave is OCTAVE_MIN, it returns False
        and doesn't change any octaves

        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.notes[5].octave
        3

        >>> hotcrossbuns = Melody("hotcrossbuns.txt")
        >>> hotcrossbuns.lower_octave()
        True
        >>> hotcrossbuns.notes[5].octave
        3

        >>> fur_elise = Melody("fur_elise.txt")
        >>> fur_elise.lower_octave()
        True
        >>> fur_elise.notes[5].octave
        3

        >>> jay_chou = Melody("jay_chou.txt")
        >>> jay_chou.lower_octave()
        True
        >>> jay_chou.notes[4].octave
        1
        """
        if has_limit_octave(self.notes, note.Note.OCTAVE_MIN, note.Note.OCTAVE_MAX):
            return False

        for i in self.notes:
            if i.pitch != 'R':
                i.octave += - 1

        return True

    def upper_octave(self):
        """ () -> bool
        Increases the octave of all notes in the song by 1
        and returns True
        If one octave is OCTAVE_MAX, it returns False
        and doesn't change any octaves

        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.upper_octave()
        True
        >>> happy_birthday.notes[5].octave
        5

        >>> hotcrossbuns = Melody("hotcrossbuns.txt")
        >>> hotcrossbuns.upper_octave()
        True
        >>> hotcrossbuns.notes[5].octave
        5

        >>> fur_elise = Melody("fur_elise.txt")
        >>> fur_elise.upper_octave()
        True
        >>> fur_elise.notes[5].octave
        5

        >>> jay_chou = Melody("jay_chou.txt")
        >>> jay_chou.upper_octave()
        True
        >>> jay_chou.notes[4].octave
        1
        """

        if has_limit_octave(self.notes, note.Note.OCTAVE_MIN, note.Note.OCTAVE_MAX):
            return False

        for i in self.notes:
            if i.pitch != 'R':
                i.octave += 1

        return True

    def change_tempo(self, multiplier):
        """ (float) -> NoneType
        Takes a positive float as input
        Multiplies the duration of each note by the input 'multiplier'

        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_tempo(0.5)
        >>> happy_birthday.get_total_duration()
        6.5

        >>> twinkle = Melody("twinkle.txt")
        >>> twinkle.change_tempo(1)
        >>> twinkle.get_total_duration()
        24.5

        >>> fur_elise = Melody("fur_elise.txt")
        >>> fur_elise.change_tempo(2)
        >>> fur_elise.get_total_duration()
        51.59999999999989

        >>> fur_elise = Melody("fur_elise.txt")
        >>> fur_elise.change_tempo(2.5645)
        >>> fur_elise.get_total_duration()
        66.16410000000016
        """

        for i in self.notes:
            i.duration = i.duration * multiplier


if __name__ == "__main__":
    doctest.testmod()


