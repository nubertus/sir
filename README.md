# SIR-Modell mit Euler-Verfahren

Dieses Programm wird im Ergänzungsfach Anwendungen der Mathematik an der ISME St. Gallen verwendet. 

Ein einfaches explizites Euler-Verfahren wird verwendet um die gekoppelten Differentialgleichungen des SIR-Modells numerisch zu lösen: 

*S' = -a S I*

*I' = a S I - b I*

*R' = b I*

Dabei sind *S* die "susceptibles", *I* die Infizierten und *R* removed. *a* und *b* sind zwei Parameter. Details findest du auf [Wikipedia](https://de.wikipedia.org/wiki/SIR-Modell).
