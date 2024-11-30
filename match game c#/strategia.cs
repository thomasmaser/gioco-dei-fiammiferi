using System;

namespace matchGame
{
    public class Strategia
    {
        public static int Computer(ref int numero)
        {
            if (numero%4 == 0){
                int rimasti = numero - 3;
                Console.WriteLine("ho tolto 3 fiammiferi, ne rimangono " + rimasti);
                return numero = rimasti;
            } else if (numero%4 == 1){
                Random random = new Random();
                int randNum = random.Next(1, 3);
                int rimasti = numero - randNum;
                Console.WriteLine("ho tolto " + randNum + " fiammiferi, ne rimangono " + rimasti);
                return numero = rimasti;
            } else{
                int num = (numero%4)-1;
                int rimasti = numero - num;
                Console.WriteLine("ho tolto " + num + " fiammiferi, ne rimangono " + rimasti);
                return numero = rimasti;
            }
        }

        public static int Utente(ref int numero)
        {
            Console.WriteLine("sta a te");
            int togli;
            do
            {
                Console.WriteLine("togli da 1 a 3 fiammiferi");
                int.TryParse(Console.ReadLine(), out togli);
            } while (togli == 0 || togli>3);
            int rimasti = numero -togli;
            Console.WriteLine("rimangono " + rimasti + " fiammiferi");
            return numero = rimasti;
        }  
    }
}