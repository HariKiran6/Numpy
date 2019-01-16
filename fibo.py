{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fibonacci sequence upto 17 :\n",
      "0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 , 89 , 144 , 233 , 377 , 610 , 987 , "
     ]
    }
   ],
   "source": [
    "nterms = 17\n",
    "\n",
    "n1 = 0\n",
    "n2 = 1\n",
    "count = 0\n",
    "\n",
    "if nterms <= 0:\n",
    "   print(\"Please enter a positive integer\")\n",
    "elif nterms == 1:\n",
    "   print(\"Fibonacci sequence upto\",nterms,\":\")\n",
    "   print(n1)\n",
    "else:\n",
    "   print(\"Fibonacci sequence upto\",nterms,\":\")\n",
    "   while count < nterms:\n",
    "       print(n1,end=' , ')\n",
    "       nth = n1 + n2\n",
    "       n1 = n2\n",
    "       n2 = nth\n",
    "       count += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
