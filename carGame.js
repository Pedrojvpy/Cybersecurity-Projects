// Simple Car Game in JavaScript - Pedro Mantovani

class Car {
    constructor(model) {
        this.model = model;
        this.speed = 0;
    }

    accelerate() {
        this.speed += 10;
        console.log(`${this.model} acelerou para ${this.speed} km/h!`);
    }

    brake() {
        this.speed -= 10;
        if (this.speed < 0) this.speed = 0;
        console.log(`${this.model} freou para ${this.speed} km/h!`);
    }
}

// Simulação de uso do carro
const myCar = new Car("McLaren JS");
console.log("Bem-vindo ao Simple Car Game em JS!");

myCar.accelerate();
myCar.accelerate();
myCar.brake();

console.log("Fim do jogo em JS.");

// Para rodar no navegador, precisaria de um arquivo HTML:
/*
<!DOCTYPE html>
<html>
<head>
    <title>Car Game JS</title>
</head>
<body>
    <script src="carGame.js"></script>
</body>
</html>
*/
