<?php
// confirmamos que los datos viene por el metodo post
if(filter_input(INPUT_POST, 'num1') && filter_input(INPUT_POST, 'num2')){
  //recogemos las variables
  $num1=filter_input(INPUT_POST, 'num1');
  $num2=filter_input(INPUT_POST, 'num2');
  
  //sumamos
  $resultado=$num1 + $num2;
  
  //imprimimos resultado
  echo "EL RESULTADO ES: ".$resultado;
}