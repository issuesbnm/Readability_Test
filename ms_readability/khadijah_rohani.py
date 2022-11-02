#from readability.exceptions import ReadabilityException

class Result:
    def __init__(self, score, grade_level):
        self.score = score
        self.grade_level = grade_level

    def __str__(self):
        return "score: {}, grade_level: '{}'". \
            format(self.score, self.grade_level)

class KhadijahRohani:
    def __init__(self, stats):
        self._stats = stats
        #if stats.num_words < 100:
        #    raise ReadabilityException('100 words required.')

    def score(self):
        score = self._score()
        return Result(
            score=score,
            grade_level=self._grade_level(score)
        )

    def _score(self):
        stats = self._stats
        return (0.3793 * stats.avg_words_per_sentence +
                0.0207 * stats.num_syllables) - 13.988

    def _grade_level(self, score):
        return str(round(score))
