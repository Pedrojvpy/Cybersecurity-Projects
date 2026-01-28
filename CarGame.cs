using System;

namespace SimpleCarGame
{
    public class Car
    {
        public string Model { get; set; }
        public int Speed { get; set; }

        public Car(string model)
        {
            Model = model;
            Speed = 0;
        }

        public void Accelerate()
        {
            Speed += 10;
            Console.WriteLine($"{Model} acelerou para {Speed} km/h!");
        }

        public void Brake()
        {
            Speed -= 10;
            if (Speed < 0) Speed = 0;
            Console.WriteLine($"{Model} freou para {Speed} km/h!");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Bem-vindo ao Simple Car Game!");
            Car myCar = new Car("Fusca Tunado");

            myCar.Accelerate();
            myCar.Accelerate();
            myCar.Brake();

            Console.WriteLine("Fim do jogo.");
        }
    }
}
