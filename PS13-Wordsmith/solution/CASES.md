# Wordsmith cases

Use letters a,c,e,i,n,r,t and a word list containing cat,crate,trace,rain,tat.

| Inputs before the deadline | Score and result |
| --- | --- |
| cat,cat,crate,:quit | 8;duplicate cat scores once |
| CAT,space-padded crate,:quit | 8;case/whitespace normalized |
| banana,notaword,empty,:quit | 0;invalid guesses rejected |
| tat,:quit | 3;letters may repeat within a word |
| cat,:quit | 3;clean early exit |
| EOF after cat | 3;clean input exit |

Timing:with start 0 and duration 60,an answer at 59.9 may score;an answer at 60 or
later does not. Before prompting at/after 60,the round ends without another read.
An answer pending while time expires is discarded when it returns.
A real-clock check can use duration 0.05 and a reader that returns after 0.1 seconds.
The starter loads its complete dictionary and leaves game construction assigned.
