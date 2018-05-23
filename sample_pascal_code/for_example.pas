program controlFor;
var
    x, y, z : integer;
begin
    y := 1;
    writeln('y is', y, 'before for-loop');
    for x := 5 to 20 do
    begin
        y := y + 1;
        writeln('y + 1 =', y);
    end;
end.
