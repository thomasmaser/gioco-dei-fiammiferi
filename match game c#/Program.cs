using matchGame;

Console.WriteLine("inizia il fottuto gioco dei fottuti fiammiferi");
int numFiammiferi;
do {
    Console.WriteLine("scegli con quanti fiammiferi vuoi giocare");
    int.TryParse(Console.ReadLine(), out numFiammiferi);
} while (numFiammiferi<3 || numFiammiferi>100);

do
{
    Strategia.Computer(ref numFiammiferi);
    if (numFiammiferi == 1){
    Console.WriteLine("hai perso, coglione!");
    } else {
        Strategia.Utente(ref numFiammiferi);
        if (numFiammiferi == 1){
            Console.WriteLine("hai vinto, ma non visualizzerai mai questo messaggio(spero)");
        }
    }
            
} while (numFiammiferi!=1);

