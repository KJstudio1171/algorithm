int gcd(int a, int b) {
	
	while(b != 0) {
		int r = a % b;
		a = b;
		b = r;
	}
	return a;
}

int gcd(int a, int b) {
	if(b == 0) return a;
	return gcd(a, a % b);
}