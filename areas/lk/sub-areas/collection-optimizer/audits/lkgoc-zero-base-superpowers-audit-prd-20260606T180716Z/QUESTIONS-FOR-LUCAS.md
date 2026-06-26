# Perguntas obrigatórias — LKGOC Zero-Base v2

Status: **Aguardando Lucas**

Responda curto, pode ser por número.

## A. Gold Source e fidelidade visual

1. O Gold Source continua sendo exatamente a coleção **New Balance 204L** atual em production?
2. A regra é copiar o shell visual da 204L com o mínimo de variação possível? Sim/não.
3. Alguma parte da 204L você **não** quer replicar nas próximas coleções?
4. O comparativo lado a lado precisa ser aprovado por você antes de cada merge, ou posso usar como gate interno e só pedir aprovação final?

## B. Puma Speedcat

5. A Puma Speedcat deve ser o primeiro rebuild zero-base?
6. Quer rollback/limpeza da Puma DEV atual antes do rebuild, ou posso sobrescrever no DEV mantendo snapshot?
7. Para Puma, você quer manter fontes como Vogue US/Vogue Brasil/Overkill, desde que encaixadas no shell 204L?
8. Há alguma imagem específica da Puma que você quer priorizar ou vetar?

## C. Conteúdo e tom

9. O guia deve seguir o mesmo nível de densidade editorial da 204L, mesmo que fique longo?
10. Você prefere copy mais moda/editorial ou mais comercial/conversão?
11. Pode mencionar motorsport/F1 como origem da Speedcat, ou prefere focar street style/moda?
12. Alguma palavra proibida além das guardrails atuais de não usar pronta entrega/encomenda/estoque como taxonomia pública?

## D. Operação e aprovação

13. Posso reconstruir no tema DEV `155065450718` sem pedir nova aprovação a cada write DEV, mantendo Production bloqueado?
14. Depois do QA visual side-by-side, você quer receber approval packet com screenshots antes de qualquer merge?
15. Você quer que eu corrija o LKGOC sistêmico primeiro e só depois reconstrua Puma, ou já posso aplicar o sistema novo na Puma após suas respostas?

## E. Próximas coleções

16. Depois da Puma, quais vêm na ordem?
   - Nike Dunk
   - Adidas Gazelle
   - Yeezy
   - Labubu
   - outra?
17. Para cada coleção, quer PRD pequeno individual ou um PRD mestre + Contract Lock individual?

## F. Critério final

18. Se o build passar tecnicamente mas você achar visualmente “não 204L”, o status oficial será FAIL. Confirmado?
19. Você quer que qualquer worker Superpowers possa vetar o PASS sem pedir permissão? Confirmado?
20. Qual é o nível de tolerância visual: 90% igual ao 204L, 95%, ou praticamente idêntico mudando só conteúdo/mídia?
