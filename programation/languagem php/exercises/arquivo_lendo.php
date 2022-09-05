<?
$teste = "xpto.txt";
$id = fopen($teste,"a+");
$conteudo = fread($id,filesize($teste));
print 'arquivo...:';
print $teste;
print "<br>";
print 'conteudo..:';
print $conteudo;
fclose($id);
?>
