     # conversion pouces/cm et cm/pouces
     # version 1 (gH)
     
     # 1. calcul à partir de quant et unit (variable resultat)
     #    si unit est "pouces" on multiplie quant par 2.54
     #    sinon on divise quant par 2.54
     
if($unit=="pouces"){
     $res=$longeur*2.54;
     $other="cm";
} else {
     $res=$longeur/2.54;
     $other="pouces";
}
     
     # 2. affichage arrondi (variable arrondi)
     #    on veut produire "3 pouces correspondent à 7.62 cm à 0.01 près"
     #    et "3.1234567*2.54 pouces correspondent à 7.93 cm à 0.01 près"

$arrondi=sprintf("%0.2f", $res);
echo "$longeur $unit = $res $other (a' 0.01)"