import re

# Função auxiliar para testar regex e mostrar resultados
def testar_regex(descricao, padrao, texto):
    print(f"\n# {descricao}")
    print(f"Regex: {padrao}")
    matches = re.findall(padrao, texto)
    print("Matches encontrados:", matches)

# 1️⃣ CPF
testar_regex("CPF", r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b",
"112.763.465-32, 987.654.321-00, 123.456.789-10, 111.111.111-11, 000-000-000-00, 222.222.222-22")

# 2️⃣ Palavras com 5 letras
testar_regex("Palavras com 5 letras", r"\b[A-Za-z]{5}\b",
"Alice Johnson, Bob Smith, Andrew Brown, Michael Anderson, Angela White, Jessica Adams")

# 3️⃣ Datas que começam com 01
testar_regex("Datas começando com 01", r"\b01/\d{2}/\d{4}\b",
"01/01/2024, 23/05/2022, 01/07/2023, 15/09/2021, 01/12/2020")

# 4️⃣ E-mails com domínio example.com
testar_regex("E-mails example.com", r"\b[A-Za-z0-9._%+-]+@example\.com\b",
"john.doe@example.com, jane.doe@gmail.com, admin@company.com, user@example.com, info@example.org")

# 5️⃣ Telefones
testar_regex("Telefones (xx) xxxx-xxxx ou (xx) xxxxx-xxxx", r"\(\d{2}\) \d{4,5}-\d{4}\b",
"(21) 1234-5678, (11) 98765-4321, (31) 8765-4321, 12345-6789, (55) 4321-1234")

# 6️⃣ Frases terminadas com !
testar_regex("Frases terminadas com !", r"[^.!?]*!", 
"Olá, mundo! Bom dia. Vamos lá! Esta é uma frase. Incrível!")

# 7️⃣ Senhas com número e caractere especial
testar_regex("Senhas com número e caractere especial", r"(?=.*\d)(?=.*[!@#$%^&*]).+", 
"senha123 password! Pass@123 secure&safe NoSpecialChar1 Valid#456")

# 8️⃣ Palavras com 5 letras (nova lista)
testar_regex("Palavras com 5 letras (nova lista)", r"\b[A-Za-z]{5}\b",
"apple, banana, grape, kiwi, mango, peach, plum")

# 9️⃣ CNPJ
testar_regex("CNPJ", r"\b\d{2}\.\d{3}\.\d{3}/0001-\d{2}\b",
"12.345.678/0001-90, 98.765.432/0001-01, 11.222.333/0001-45, 44.555.666/0001-78, 00-000-000/0001-00, 77.888.999/0001-99")

# 🔟 CEP
testar_regex("CEP", r"\b\d{5}-\d{3}\b",
"12345-678, 98765-432, 00000-000, 45678-901, 11111-222")

# 11️⃣ Palavras com 3 letras
testar_regex("Palavras com 3 letras", r"\b[A-Za-z]{3}\b",
"The cat and dog run fast, but the fox is quick.")

# 12️⃣ Datas terminando em 2023
testar_regex("Datas terminando em 2023", r"\b\d{2}-\d{2}-2023\b",
"15-04-2023, 22-11-2022, 01-01-2023, 30-06-2021, 12-12-2023")

# 13️⃣ URLs https://
testar_regex("URLs https://", r"\bhttps://\S+\b",
"https://example.com, http://test.com, https://site.org, ftp://server.com, https://myapp.net")

# 14️⃣ Frases terminadas com ?
testar_regex("Frases terminadas com ?", r"[^.!?]*\?", 
"Como você está? Tudo bem. O que fazer? Vamos agora! Onde está?")

# 15️⃣ Horários válidos
testar_regex("Horários válidos HH:MM", r"\b(?:[01]\d|2[0-3]):[0-5]\d\b",
"08:30, 14:45, 25:60, 23:59, 00:00, 12:75, 19:30")

# 16️⃣ Placas ABC-1234
testar_regex("Placas ABC-1234", r"\b[A-Za-z]{3}-\d{4}\b",
"ABC-1234, XYZ-9876, 123-ABCD, DEF-5678, GHI-0000, JKL-4321, MNO-PQRS")

# 17️⃣ Códigos PRD + 4 dígitos
testar_regex("Códigos PRD + 4 dígitos", r"\bPRD\d{4}\b",
"PRD1234, ABC5678, PRD9999, XYZ0001, PRD0000, DEF1111, PRD7890")

# 18️⃣ Senhas fortes
testar_regex("Senhas fortes", r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$",
"Password1! senha123 SENHA! Abc123@ p@ssW0rd 12345678 MinhaSenh@1")

# 19️⃣ Endereços IP válidos
testar_regex("Endereços IP válidos", r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d{1,2})\.){3}(?:25[0-5]|2[0-4]\d|1?\d{1,2})\b",
"192.168.1.1, 256.300.400.500, 127.0.0.1, 10.0.0.255, 999.999.999.999, 172.16.254.1, 0.0.0.0")

# 20️⃣ Cartões Visa
testar_regex("Cartões Visa", r"\b4(?:[ -]?\d){12}(?:[ -]?\d{3}){0,2}\b",
"4111-1111-1111-1111, 5555 5555 5555 4444, 4000123456789, 3111111111111111, 4111 1111 1111 1111 111, 4000-1234-5678-9012-345")



"""
VOU SUBIR O ARQUIVO TAMBÉM NO GITHUB PARA O SENHOR TESTAR

O BASH É : python regex_testes.py


"""