#
# Algarismos indo-arabicos -> romanos
#    1 -> I
#    2 -> II
#    3 -> III
#    4 -> IV
#    5 -> V
#   10 -> X
#   50 -> L
#  100 -> C
#  500 -> D
# 1000 -> M
# 
from romanos import *

def test_retorna_I():
	assert romanos(1) == 'I'

def test_retorna_II():
	assert romanos(2) == 'II'
	
def test_retorna_III():
	assert romanos(3) == 'III'
	
def test_retorna_IV():
	assert romanos(4) == 'IV'

def test_retorna_V():
	assert romanos(5) == 'V' 

def test_retorna_VI():
	assert romanos(6) == 'VI' 

def test_retorna_VII():
	assert romanos(7) == 'VII'

def test_retorna_VIII():
	assert romanos(8) == 'VIII'
	
def test_retorna_IX():
	assert romanos(9) == 'IX'
	
def test_retorna_X():
	assert romanos(10) == 'X'

def test_retorna_XI():
	assert romanos(11) == 'XI'
