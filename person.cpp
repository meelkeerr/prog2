#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
        int fib();
	private:
		int age;
        int 1fib( int n);
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}

int fib(){
    return 1fib(age);
}

int 1fib(int age){
    if(age <= 1){
        return age;
    }
    else{
        return 1fib(age - 1) + 1fib(age - 2);
    }
}


extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
    int Person_fib(Person* person){return person -> fib();}
	}