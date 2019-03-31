#include <iostream>
#include <thread>
using namespace std;

void f(int& x)
{
  cout << &x << endl;
}

int main()
{
  int x = 33;
  f(x);
  thread t(f, ref(x));
  t.join();
}
