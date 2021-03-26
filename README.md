# DNA Forensics

Write the functions described in `exercise.py`. 

DNA has been used in criminal justice for decades. DNA can be considered just a
sequence of four different bases: adenine (A), cytosine (C), guanine (G), or
thymine (T). Some portions of this sequence are the same, or at least very
similar, across almost all humans, but other portions of the sequence have a
higher genetic diversity and thus vary more across the population.

One place where DNA tends to have high genetic diversity is in Short Tandem
Repeats (STRs). An STR is a short sequence of DNA that tends to be repeated
back-to-back numerous times at specific locations in DNA. The number of times
any particular STR repeats varies a lot among different people. In the DNA
samples below, for example, Alice has the STR AGAT repeated four times in her
DNA, while Bob has the same STR repeated five times.

```
Ada: CTAGATAGATAGATAGATGACTA
         ^..^^..^^..^^..^
Bia: CTAGATAGATAGATAGATAGATT
       ^..^^..^^..^^..^^..^
```

Using multiple STRs, rather than just one, can improve the accuracy of DNA
profiling. If the probability that two people have the same number of repeats
for a single STR is 5%, and the analyst looks at 10 different STRs, then the
probability that two DNA samples match purely by chance is about 1 in 1
quadrillion (assuming all STRs are independent of each other). So if two DNA
samples match in the number of repeats for each of the STRs, the analyst can be
pretty confident they came from the same person. CODIS, The FBI's DNA database,
uses 20 different STRs as part of its DNA profiling process.

For example, a DNA database could be formatted as a Comma Separated Values (CSV)
file, like this:

```
name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25
```

The data in the above file would suggest that Alice has the sequence AGAT
repeated 28 times consecutively somewhere in her DNA, the sequence AATG repeated
42 times, and TATC repeated 14 times. Bob, meanwhile, has those same three STRs
repeated 17 times, 22 times, and 19 times, respectively. And Charlie has those
same three STRs repeated 36, 18, and 25 times, respectively.

The goal of the exercise is to build a class `Profiler` which encapsulates a DNA
sequence and the methods: for computing the longest run of an STR
(`longest_run`), and for evaluating whether a suspect with a known DNA profile
matches the sequence or not (`match_suspect`).

```python3
```



You can test your solution locally by running: `python exercise.py`

Since I'm not a biologist, the biological terminology is probably not accurate:
please, suggest corrections on Zulip!
