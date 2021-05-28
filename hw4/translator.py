import re


letters = {  
ord('а'): 'a',
ord('А'): 'A',
ord('б'): 'b', 
ord('Б'): 'B',
ord('в'): 'v',
ord('В'): 'V',
ord('г'): 'g',
ord('Г'): 'G',
ord('д'): 'd',
ord('Д'): 'D',
ord('е'): 'e',
ord('Е'): 'E',
ord('ё'): 'yo',
ord('Ё'): 'Yo',
ord('ж'): 'zh',
ord('Ж'): 'Zh',
ord('з'): 'z',
ord('З'): 'Z',
ord('и'): 'i',
ord('И'): 'I',
ord('й'): 'y',
ord('Й'): 'Y',
ord('к'): 'k',
ord('К'): 'K',
ord('л'): 'l',
ord('Л'): 'L',
ord('м'): 'm',
ord('М'): 'M',
ord('н'): 'n',
ord('Н'): 'N',
ord('о'): 'o',
ord('О'): 'O',
ord('п'): 'p',
ord('П'): 'P',
ord('р'): 'r',
ord('Р'): 'R',
ord('с'): 's',
ord('С'): 'S',
ord('т'): 't',
ord('Т'): 'T',
ord('у'): 'u',
ord('У'): 'U',
ord('ф'): 'f',
ord('Ф'): 'F',
ord('х'): 'h',
ord('Х'): 'H',
ord('ц'): 'ts',
ord('Ц'): 'Ts',
ord('ч'): 'ch',
ord('Ч'): 'Ch',
ord('ш'): 'sh',
ord('Ш'): 'Sh',
ord('щ'): 'sh',
ord('Щ'): 'Sh',
ord('ы'): 'y',
ord('Ы'): 'Y',
ord('ь'): '`',
ord('Ь'): '`',
ord('ъ'): '`',
ord('Ъ'): '`',
ord('э'): 'e',
ord('Э'): 'E',
ord('ю'): 'yu',
ord('Ю'): 'Yu',
ord('я'): 'ya',
ord('Я'): 'Ya',
}

def normalize(string):
	'''
	This function converts kirilica to latinica
	'''
	# Регулярка (все цифры и буквы, кроме пробела и апострофа)
	WITHOUT_SYMBOL_REGEX = re.compile(r"[^a-z^A-Z^0-9' ''`']")

	translated = string.translate(letters)

	string_without_symbols = re.sub(WITHOUT_SYMBOL_REGEX, '_', translated)

	return string_without_symbols

