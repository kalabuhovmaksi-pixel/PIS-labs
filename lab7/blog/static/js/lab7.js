function showSum() {
    var a = 2;
    var b = 3;
    var c = a + b;
    var p = document.getElementById("result");
    p.innerHTML = "2 + 3 = " + c;
}

function toggleColor() {
    var p = document.getElementById("result");
    if (p.style.color === "red") {
        p.style.color = "black";
    } else {
        p.style.color = "red";
    }
}

function askAge() {
    var input = prompt("Сколько вам лет?");
    if (input === null) {
        return;
    }

    var age = parseInt(input);

    if (isNaN(age)) {
        alert("Нужно ввести число.");
        return;
    }

    if (age < 18) {
        alert("Вам меньше 18 лет.");
    } else {
        alert("Вам 18 или больше.");
    }
}
