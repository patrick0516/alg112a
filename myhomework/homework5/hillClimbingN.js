function hillClimbing(f, p, h = 0.01) {             //h為步進值，p為當前點，f為目標
    let failCount = 0;

    while (failCount < 10000) {
        const fnow = f(p);
        const [p1, f1] = neighbor(f, p, h);

        if (f1 >= fnow) {
            failCount = 0;
            p = p1;
            console.log('p=', p, 'f(p)=', f1);
        } else {
            failCount++;
        }
    }

    return { p, fnow };
}

function neighbor(f, p, h) {
    const dimensions = p.length;
    const p1 = p.slice();

    const index = Math.floor(Math.random() * dimensions);
    p1[index] += (Math.random() - 0.5) * h;

    const f1 = f(...p1);
    return [p1, f1];
}

function f(x, y, z) {
    return -1 * (x ** 2 + y ** 2 + z ** 2);
}

const result = hillClimbing(f, [2, 1, 3]);
console.log(result);
