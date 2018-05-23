program controlWhile;
    var x, y : integer;
begin
    x := 0;
    writeln('initial value of x:', x);
    while x < 10 do
        begin
            x := x + 5;
            writeln('value of x are x + 5 =', x);
        end;
    writeln('final value of x:', x);
end.
