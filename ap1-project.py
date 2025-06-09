print('Seja muito bem-vindo ao Show do Milhão da área de TECNOLOGIA! Infelizmente você não receber dinheiro, mas pode descobrir qual área é a certa para você!\nSerão feitas 15 perguntas sobre seu gosto pessoal na área de tecnologia, que lhe diram qual combina melhor com você, sendo elas:\n1- ÁREA DE DESENVOLVIMENTO DE SOFTWARE\n2- ÁREA DE PRODUTOS (UX/UI, Product Owner, Product Manager, etc.)\n3- ÁREA DE QUALIDADE (Testes, QA, automação de testes, etc.)\nVocê deve responder as alternativas com um número de 1 à 5, onde 1 significa Discordo Totalmente e 5 significaria Concordo Totalmente. \nEntendido? Espero que sim! Vamos lá!')
#ÁREA DE DESENVOLVIMENTO DE SOFTWARE
answer1 = int(input('\n>>> Começando o Show do Milhão! <<<\n-> Primera pergunta! \n//Gosto de programar e resolver problemas com código.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
answer2 = int(input('\n-> Pergunta número #2! \n//Tenho interesse em criar aplicativos e sites.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
answer3 = int(input('\n-> Pergunta número #3! \n//Gosto de aprender novas linguagens de programação.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
answer4 = int(input('\n-> Pergunta número #4! \n//Prefiro trabalhar com lógica e estruturação de código.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
answer5 = int(input('\n-> Pergunta número #5! \n//Tenho paciência para depurar erros e otimizar código.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
#ÁREA DE PRODUTOS
answer6 = int(input('\n-> Pergunta número #6! \n//Gosto de pensar na experiência do usuário ao usar um sistema.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
answer7 = int(input('\n-> Pergunta número #7! \n//Tenho interesse em pesquisa de mercado e comportamento do usuário.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
answer8 = int(input('\n-> Pergunta número #8! \n//Me interesso por criar soluções inovadoras e intuitivas.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
answer9 = int(input('\n-> Pergunta número #9! \n//Gosto de trabalhar com design, wireframes ou prototipagem.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
answer10 = int(input('\n-> Pergunta número #10! \n//Quero entender e definir estratégias para melhorar produtos digitais.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
#ÁREA DE QUALIDADE
answer11 = int(input('\n-> Pergunta número #11! \n//Gosto de testar e garantir que sistemas funcionem corretamente.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
answer12 = int(input('\n-> Pergunta número #12! \n//Tenho interesse em encontrar erros e melhorar a estabilidade dos produtos.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
answer13 = int(input('\n-> Pergunta número #13! \n//Acredito que testes automatizados ajudam a evitar falhas em sistemas.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
answer14 = int(input('\n-> Pergunta número #14! \n//Gosto de seguir padrões e documentar processos para garantir qualidade.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
answer15 = int(input('\n-> Pergunta número #15! \n//Quero trabalhar garantindo que um software funcione bem para todos os usuários.\n1)Discordo Totalmente\n2)Discordo\n3)Neutro\n4)Concordo\n5)Concordo Totalmente\nSua resposta é:'))
if 1 <= answer1 <= 5 and 1 <= answer2 <= 5 and 1 <= answer3 <= 5 and 1 <= answer4 <= 5 and 1 <= answer5 <=5 and 1 <= answer6 <= 5 and 1 <= answer7 <= 5 and 1 <= answer8 <= 5 and 1 <= answer9 <= 5 and 1 <= answer10 <=5 and 1 <= answer11 <= 5 and 1 <= answer12 <= 5 and 1 <= answer13 <= 5 and 1 <= answer14 <= 5 and 1 <= answer15 <=5:
    pts_dev = answer1 + answer2 + answer3 + answer4 + answer5
    pts_prod = answer6 + answer7 + answer8 + answer9 + answer10
    pts_quali = answer11 + answer12 + answer13 + answer14 + answer15
    maxpts = max(pts_dev, pts_prod, pts_quali)
if pts_dev == maxpts:
    print('\nAvaliando sua pontuação, você possui uma afinidade com a ÁREA DE DESENVOLVIMENTO DE SOFTWARE, tendo um total de', pts_dev, 'pontos.')
if pts_prod == maxpts:
    print('\nAvaliando sua pontuação, você possui uma afinidade com a ÁREA DE PRODUTOS, tendo um total de', pts_prod, 'pontos.')
if pts_quali == maxpts:
    print('\nAvaliando sua pontuação, você possui uma afinidade com a ÁREA DE QUALIDADE, tendo um total de', pts_quali, 'pontos.')
else:
    print('Tente Novamente!')