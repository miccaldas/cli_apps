#!/usr/bin/env sh

sed -re "s/\\\\n/ /g" spider_results.txt > res0.txt
sed -re "s/\\\//g" res0.txt > res1.txt
# sed -re "s/]//g" res1.txt > res2.txt
sed -re "s/ ''//g" res1.txt > res3.txt
sed -re "s/ '\)/'\)/g" res3.txt > res4.txt
sed -re "s/,,/,/g" res4.txt > res5.txt
# sed -re 's/",/,/g' res5.txt > res6.txt
# sed -re "s/.,/, /g" res5.txt > res7.txt
# sed -re "s/,./, /g" res7.txt > res8.txt
sed -re "s/ ,.,/. /g" res5.txt > res9.txt
sed -re 's/ ,"/"/g' res9.txt > res10.txt
sed -re 's/"//g' res10.txt > res11.txt
sed -re "s/ , /, /g" res11.txt > res12.txt
sed -re "s/\( ,  '  ,  ' //g" res12.txt > res13.txt

sed -re "s/\(,  '  ,  ' //g" res13.txt > res15.txt
sed -re "s/' , '//g" res15.txt > res16.txt
sed -re "s/ ',  /, /g" res16.txt > res17.txt
sed -re "s/,  /, /g" res17.txt > res18.txt
sed -re "s/ , /, /g" res18.txt > res19.txt
sed -re "s/'//g" res19.txt > res20.txt
sed -re "s/ ., //g" res20.txt > res21.txt
# sed -re "s/., /, /g" res21.txt > res22.txt
sed -re "s/, ,//g" res21.txt > res22.txt
sed -re "s/^\(,   /\(/g" res22.txt > res23.txt
sed -re "s/.,,/, /g" res23.txt > res24.txt
sed -re "s/  / /g" res24.txt > res25.txt
sed -re "s/([[:alpha:]]),([[:alpha:]])/\1, \2/g" res25.txt > res26.txt
sed -re "s/\[description , /\[/g" res26.txt > res27.txt
sed -re "s/ , / /g" res27.txt > res28.txt
sed -re 's/([[:punct:]])(https.*$)/\1 \2/g' res28.txt > res30.txt
sed -re 's/([[:punct:]])( https.*$)/\1],\2/g' res30.txt > res31.txt
sed -re "s/\(//g" res31.txt > res32.txt
sed -re "s/\)//g" res32.txt > res33.txt
mv res33.txt final_text.txt
