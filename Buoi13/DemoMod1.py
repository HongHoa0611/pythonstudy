{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "69a2274f-caa9-4bb4-b180-19d337c01c1a",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'MyModule' has no attribute 'greeting'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[4], line 5\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mMyModule\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;124;03m''' import <TenFile> # Chèn tất cả các thành phần trong module\u001b[39;00m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;124;03mGọi 1 cái cụ thể: <TenFile/TenModule>.Ten_Thanh_Phan'''\u001b[39;00m\n\u001b[1;32m----> 5\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43mMyModule\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mgreeting\u001b[49m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mTèo\u001b[39m\u001b[38;5;124m'\u001b[39m))\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'MyModule' has no attribute 'greeting'"
     ]
    }
   ],
   "source": [
    " import MyModule\n",
    "''' import <TenFile> # Chèn tất cả các thành phần trong module\n",
    " Gọi 1 cái cụ thể: <TenFile/TenModule>.Ten_Thanh_Phan'''\n",
    "\n",
    "print(MyModule.LUONG_CO_BAN)\n",
    "print(MyModule.greeting('Tèo'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb3e7431-68fb-4979-831e-e82bbde4149e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df997b53-d3de-4333-beef-5bda4d39d511",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
