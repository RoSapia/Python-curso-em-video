N = int(input())
hora = int(N / 3600)
minuto = int((N -(hora * 3600)) / 60)
segundo = int(N % 60)

print('{}:{}:{}'.format(hora, minuto, segundo))


#total = 685;
#$horas = floor($total / 3600);
#$minutos = floor(($total - ($horas * 3600)) / 60);
#$segundos = floor($total % 60);
#echo $horas . ":" . $minutos . ":" . $segundos;