# Samy Sabir 261119166

import doctest
import musicalbeeps


class Note:
    """Contains information about a single music note.

    Class attributes:
    *OCTAVE_MIN = 1
    *OCTAVE_MAX = 7

    Instance attributes:
    *duration = float
    *pitch = str
    *octave = int
    *accidental = str
    """

    OCTAVE_MIN = 1
    OCTAVE_MAX = 7

    def __init__(self, duration, pitch, octave=OCTAVE_MIN, accidental='natural'):
        """ (float, str, int, str) -> NoneType
        Creates an object of type Note
        Raises an AssertionError if any of the inputs is not in the correct format

        >>> note = Note(2.0, "B", 4, "natural")
        >>> note.pitch
        'B'

        >>> note = Note(2.0, "V", 4, "natural")
        Traceback (most recent call last):
        AssertionError: Pitch is either not of the right type or not a valid pitch letter.

        >>> note = Note(2.0, "B", 8, "natural")
        Traceback (most recent call last):
        AssertionError: Octave is either greater than 7 or less than 1.

        >>> note = Note(2.0, "B", 4, "round")
        Traceback (most recent call last):
        AssertionError: Accidental Value is either not of the right type or not 'sharp', 'flat' or 'natural'.
        """

        self.duration = duration
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental

        if type(duration) != float or type(octave) != int or duration <= 0:
            raise AssertionError("One of the inputs is not of the right type.")

        if pitch not in ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'R']:
            raise AssertionError("Pitch is either not of the right type or not a valid pitch letter.")

        if octave < Note.OCTAVE_MIN or octave > Note.OCTAVE_MAX:
            raise AssertionError("Octave is either greater than 7 or less than 1.")

        if accidental not in ['sharp', 'flat', 'natural']:
            raise AssertionError(
                "Accidental Value is either not of the right type or not 'sharp', 'flat' or 'natural'.")

    def __str__(self):
        """() -> str
        Returns a string of the format 'DURATION PITCH OCTAVE ACCIDENTAL'
        where each variable refers to the appropriate instance attribute

        >>> note = Note(2.0, "B", 4, "natural")
        >>> print(note)
        2.0 B 4 natural

        >>> note = Note(2.0, "R")
        >>> print(note)
        2.0 R 1 natural

        >>> note = Note(2.0, "X", 4, "natural")
        Traceback (most recent call last):
        AssertionError: Pitch is either not of the right type or not a valid pitch letter.
        """

        return str(self.duration) + ' ' + self.pitch + ' ' + str(self.octave) + ' ' + self.accidental

    def play(self, player):
        """ (Player) -> NoneType
        Takes a music player object as input
        Constructs the note string
        Passes the note string and duration to play_note method for it to play
        """
        if self.pitch == 'R':
            note_str = 'pause'

        elif self.accidental == 'flat':
            note_str = self.pitch + str(self.octave) + 'b'
        elif self.accidental == 'sharp':
            note_str = self.pitch + str(self.octave) + '#'
        else:
            note_str = self.pitch + str(self.octave)

        player.play_note(note_str, self.duration)


if __name__ == "__main__":
    doctest.testmod()
