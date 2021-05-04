# mab

Unknown Arms - Have never been pulled
Known Arms - Have been pulled once
Well Known Arms - Have had at least 2 pulls of different results or 3 pulls

Conditions are set such that the balance of selection bias between unknown arms, known arms, and well known arms always ensures most arms "catch up" with respect to collection a foundation of data on them. The code moves from balance unknown vs. known, and finally to well-known vs. known, with some mix between those two states in between of bouncing between unknown, known, and well-known. Right now, the two "bookend" states have a bias_check which is just modulo 2 of an interval moving up to bounce back and forth between unknown and known, and within the known state it bounces between known and well-known.
