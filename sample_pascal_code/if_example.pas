program controlIf;
    var x, y : integer;
begin
    x := 9;
    y := 15;
    if x > y then
        writeln('x > y;', 'x is', x, 'y is', y)
    else if x < y then
        writeln('x < y;', 'x is', x, 'y is', y)
    else
        writeln('x = y;', 'x is', x, 'y is', y);
end.
