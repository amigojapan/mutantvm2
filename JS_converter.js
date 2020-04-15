var program="var a=1;b=a+1;Console.print(b);dsfdsfd;";
lines=program.split(";");
for(var line in lines) {
	try{
		eval(line);
	} catch (error) {
		Console.print(error);
	}
}
