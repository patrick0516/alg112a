function perm(n) {
    let p = [];
    permNext(n, p);
}

function permNext(n, p) {
    let i = p.length;

    if (i === n) {
        console.log(p);
        return;
    }

    for (let x = 0; x < n; x++) {
        if (!p.includes(x)) {
            p.push(x);
            permNext(n, p);
            p.pop();
        }
    }
}

perm(2); // 列出 2 個的排列
perm(3); // 列出 3 個的排列
perm(4); // 列出 4 個的排列
perm(5); // 列出 5 個的排列
