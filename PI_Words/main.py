#!/usr/bin/python3
import sys
import os
import logging
from PI_Words.PI.PiGenerator import PiGenerator
from PI_Words.PI import BaseTranslator
from PI_Words.PI.DigitsToStringConverter import DigitsToStringConverter
from PI_Words.PI.AlphabetGenerator import AlphabetGenerator
from PI_Words.PI.WordFinder import WordFinder

class Main:
    PI_PRECISION = 1000

    # List borrowed from: http://www.langmaker.com/wordlist/basiclex.htm

    def __init__(self):
        self.WORD_LIST = []
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        words_file = open(os.path.join(self.__location__, "words.list"), "r")
        for line in words_file:
            self.WORD_LIST.append(words_file.readline)
        words_file.close()

    BASIC_ALPHABET =[
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # @staticmethod
    def main(self, *args):
        logging.basicConfig(level=logging.INFO, filename=os.path.join(self.__location__, "log"))

        print("Problem 1: Calculating Pi...")
        piHexDigits = PiGenerator.computePiInHex(self.PI_PRECISION)
        try:
            print(
                "Digits of Pi in base-16: %s\n\n" %
                    self.MaybeTruncateString(str(piHexDigits), 100))
        except:
            pass

        print("Problem 2: Translating Pi to base-26...")
        translatedPiBase26 = \
                BaseTranslator.convertBase(piHexDigits, 16, 26, self.PI_PRECISION)
        try:
            print(
                "Digits of Pi in base-26: %s\n\n" %
                    self.MaybeTruncateString(str(translatedPiBase26), 50))
        except:
            pass

        print("Problem 3: Converting Pi using basic alphabet")
        basicConversion = DigitsToStringConverter.convertDigitsToString(
                translatedPiBase26, 26, self.BASIC_ALPHABET)
        try:
            print(
                "Digits of Pi translated into a-z: %s\n\n",
                    self.MaybeTruncateString(basicConversion, 50))
        except:
            pass

        print("Problem 4: Getting word matches")
        basicSubstrings = WordFinder.getSubstrings(basicConversion, self.WORD_LIST)
        print("  ---- commented out -----")
        # for entry in basicSubstrings.entrySet():
        #     printWithContext(basicConversion, entry.getValue(), entry.getKey(), 3, true)

        try:
            print("Word coverage using basic alphabet: %d\n\n" %
                    len(basicSubstrings) / len(self.WORD_LIST))
        except:
            print(basicSubstrings)

        print('''Problem 5: Getting word matches with base-100 and
        		           frequency dictionary''')
        translatedPiBase100 = \
                BaseTranslator.convertBase(piHexDigits, 16, 100, self.PI_PRECISION)
        alphabet = AlphabetGenerator.generateFrequencyAlphabet(
                100, self.WORD_LIST)

        print("Frequency dictionary generated: %s\n" %
                          self.MaybeTruncateString(str(alphabet), 50))

        frequencyConversion = \
                DigitsToStringConverter.convertDigitsToString(
                        translatedPiBase100, 100, alphabet)
        try:
            print(
                "Digits of Pi translated into a-z: %s\n" %
                self.MaybeTruncateString(frequencyConversion, 50))
        except:
            pass

        frequencySubstrings = \
                WordFinder.getSubstrings(frequencyConversion, self.WORD_LIST)
        # for (Map.Entry<String, Integer> entry :
        #      frequencySubstrings.entrySet()) {
        #     printWithContext(frequencyConversion, entry.getValue(),
        #                      entry.getKey(), 3, true)
        # }
        try:
            print("Word coverage using frequency alphabet: %d\n\n" %
                len(frequencySubstrings) / len(self.WORD_LIST) )
        except:
            pass


     # If the input is less than or equal to len letters long, return it
     # unchanged. If the input is greater than len letters long, trim it to
     # len letters, then add an ellipses to the end.
     # 
     # @param input String to maybe truncate.
     # @param len Length to truncate to.
     # @return The input, potentially truncated to len letters with a trailing
     #         ellipses.
    def verifyinput(func):
        return func

    @staticmethod
    @verifyinput
    def MaybeTruncateString(fullinput, maxlen):
        if len(fullinput) > maxlen:
            truncated  = fullinput[0:maxlen] + "..."
            return truncated
        else:
            return fullinput


    # Pretty print a substring of a string with some context information to
    # either side.
    # 
    # @param haystack String to print from.
    # @param offset Index to start the substring in haystack.
    # @param needle The substring that should be printed from haystack.
    # @param shouldOffset If true, offset output with a leading tab char.
    # @param numContext Max amount of context characters to take from either
                      # end of the substring.

    # void printWithContext(String haystack, int offset,
    #                                       String needle, int numContext,
    #                                       boolean shouldOffset) {
    #       if (offset < 0 || offset + needle.length() > haystack.length() ||
    #           needle.length() < 0) {
    #           return
    #       }

    #       int substringStart = Math.max(0, offset - numContext)
    #       int substringEnd = Math.min(haystack.length(),
    #                                   offset + needle.length() + numContext)

    #       print("%sSubstring '%s' found at index %d: %s%s%s\n",
    #                         (shouldOffset) ? "\t" : "",
    #                         needle, offset,
    #                         (substringStart > 0) ? "..." : "",
    #                         haystack.substring(substringStart, substringEnd),
    #                         (substringEnd < haystack.length()) ? "..." : "")

if __name__ == "__main__":
    m = Main()
    m.main()

