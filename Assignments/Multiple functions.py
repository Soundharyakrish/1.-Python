{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "d0ffd914-94a0-46ca-bee3-909f26745f21",
   "metadata": {},
   "outputs": [],
   "source": [
    "class multiplefunctions():\n",
    "    def Subfields():\n",
    "        print(\"Subfields in AI are:\")\n",
    "        for Subfields in lists:\n",
    "            print(Subfields)\n",
    "    def oddeven():\n",
    "        num=int(input(\"Enter the number:\"))\n",
    "        if((num%2)==1):\n",
    "            print(\"odd number\")\n",
    "            message=\"odd number\"\n",
    "        else:\n",
    "            print(\"even number\")\n",
    "            message=\"even number\"\n",
    "    def Eligible():\n",
    "        num=int(input(\"Enter the age:\"))\n",
    "        if (age>18):\n",
    "            print(\"Eligible for marriage\")\n",
    "        else:\n",
    "            print(\"Not Eligible for marraige\")\n",
    "    def Percentage():\n",
    "        Subject1=int(input(\"Subject1:\"))\n",
    "        Subject2=int(input(\"Subject2:\"))\n",
    "        Subject3=int(input(\"Subject3:\"))\n",
    "        Subject4=int(input(\"Subject4:\"))\n",
    "        Subject5=int(input(\"Subject5:\"))\n",
    "        Total=Subject1+Subject2+Subject3+Subject4+Subject5\n",
    "        Percentage=(Total/500)*100\n",
    "        print(Total,\"Total\")\n",
    "        print(Percentage,\"Percentage\")\n",
    "    def triangle():\n",
    "        # Area of triange\n",
    "        Height=int(input(\"Height:\"))\n",
    "        Breadth=int(input(\"Breadth:\"))\n",
    "        print(\"Area formula:(Height*Breadth)/2\")\n",
    "        Area=(Height*Breadth)/2\n",
    "        print(\"Area of triangle\", Area)\n",
    "    \n",
    "        # Perimeter of triangle\n",
    "        Height1=int(input(\"Height1:\"))\n",
    "        Height2=int(input(\"Height2:\"))\n",
    "        Height3=int(input(\"Height3:\"))\n",
    "        print(\"perimeter formula:Height1+Height2+Height3\")\n",
    "        perimeter=Height1+Height2+Height3\n",
    "        print(\"Perimeter of triangle\", perimeter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b2bebb2e-9ffb-4959-9ad0-15c47596485d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the number: 48\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "even number\n"
     ]
    }
   ],
   "source": [
    "multiplefunctions.oddeven()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "2df3525a-a433-4681-8ac5-91efed1d0c1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Subject1: 98\n",
      "Subject2: 87\n",
      "Subject3: 95\n",
      "Subject4: 95\n",
      "Subject5: 93\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "468 Total\n",
      "93.60000000000001 Percentage\n"
     ]
    }
   ],
   "source": [
    "multiplefunctions.Percentage()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e02679f-214c-4198-8afb-acf362ab63d5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
