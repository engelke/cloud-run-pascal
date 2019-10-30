program roman(input, output);

var y: integer;

begin
   read(y);
   while y>=1000 do
      begin write('M'); y := y-1000 end;
   if y>=500 then
      begin write('D'); y := y-500 end;
   while y>=100 do
      begin write('C'); y := y-100 end;
   if y>=50 then
      begin write('L'); y := y-50 end;
   while y>=10 do
      begin write('X'); y := y-10 end;
   if y>=5 then
      begin write('V'); y := y-5 end;
   while y>=1 do
      begin write('I'); y := y-1 end;
end.