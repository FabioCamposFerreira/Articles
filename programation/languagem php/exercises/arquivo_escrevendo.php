<?
$teste = "xpto.txt";
$id = fopen($teste,"a");
$varData = date('d/m/Y');
$varHora=date('h:m:s');
$conteudo=("GRAVOU em ".$varData."&nbsp; no horario &nbsp;".$varHora);
fwrite($id,$conteudo,80);
fclose($id);
?>
