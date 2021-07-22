{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d80b957e-392f-456e-9755-0e3041f4b923",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "13 7\n"
     ]
    }
   ],
   "source": [
    "a=10\n",
    "b=3\n",
    "print(a+b, end=\" \")\n",
    "print(a-b)\n",
    "# 주석은 #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "0d2607f2-0578-4cd0-97ed-f0a8b6098a0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "13\n",
      "7\n",
      "30\n",
      "3.3333333333333335\n",
      "3\n",
      "1\n",
      "1000\n"
     ]
    }
   ],
   "source": [
    "print(a+b)\n",
    "print(a-b)\n",
    "print(a*b)\n",
    "print(a/b)\n",
    "print(a//b)\n",
    "# 실수값으로 나오는 몫을 정수로 형변환\n",
    "print(a%b)\n",
    "print(a**b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f6bbfd20-4ecb-4f67-967c-b74875c72b89",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "**********\n"
     ]
    }
   ],
   "source": [
    "s=\"*\"\n",
    "print(s*10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b98227c5-5302-485d-9307-41a8e6df7016",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "가*\n",
      "10*\n"
     ]
    }
   ],
   "source": [
    "print('가'+s)\n",
    "print(str(a)+s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "5eb7000d-60cd-4f5e-aff2-3d780e1071b1",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-16-98f42216cd69>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-16-98f42216cd69>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    print(a++)\u001b[0m\n\u001b[1;37m             ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "print(a++)\n",
    "print(a--)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "49c0578d-aea1-47f7-be46-324ff8b52ed7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n",
      "11\n",
      "10\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "a+=1\n",
    "print(a)\n",
    "print(a)\n",
    "a-=1\n",
    "print(a)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "f5984342-7de7-4475-b25b-a6f43608042c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(a>5) and (b>5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "5a8e20c4-b314-4cc1-8331-e6120ff08a6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a>>2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "bbbe4cad-cd0d-42a1-afdd-891698fbf192",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "1==True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "e95a395a-e318-4613-934f-3ba6ec4e9a8d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "0==False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "ac4baaa2-d088-41fb-b472-52b3bef834b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'> <class 'float'> <class 'str'>\n"
     ]
    }
   ],
   "source": [
    "a=10\n",
    "b=3.5\n",
    "c='a'\n",
    "print(type(a), type(b), type(c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "1cf45874-441d-4992-a26c-1a6b2f1b9600",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "age= 20\n",
      "age=20 / name=홍길동\n"
     ]
    }
   ],
   "source": [
    "age=20\n",
    "name='홍길동'\n",
    "print('age=',age)\n",
    "print('age=%d / name=%s' %(age, name))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48d3ca66-fb65-49a1-80a8-205229367bce",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3954c19b-ba6b-4035-9780-f2bf66e4aa1b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dba88c87-faf8-4d36-9011-287b20af0bfa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
