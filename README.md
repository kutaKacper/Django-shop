## Architektura informatyczna

Aplikacja składa się z wielu podaplikacji, odpowiadających za zarządzanie poszczególnymi funkcjonalnościami sklepu. Zaprojektowane są one zgodnie z modelem MVT. Każda aplikacja składa się z plików:
- models.py – zawiera klasy tworzące modele danych;
- views.py – służy do definiowania widoków aplikacji;
- admin.py – definiuje klasy reprezentujące modele dostępne do zarządzania przez panel administracyjny. Pozwala administratorom na dodawanie, edycję i usuwanie danych bezpośrednio z interfejsu panelu administracyjnego;
- apps.py – pozwala na określenie niestandardowej konfiguracji i ustawień dla danej aplikacji;
- tests.py – służy do tworzenia testów jednostkowych. Pozwalają one na weryfikację poprawności kodu, a co za tym idzie zapewnienie stabilności i niezawodności aplikacji.

Aplikacje powiązane są z bazą danych poprzez modele danych i operacje CRUD. Każda klasa modelu reprezentuje tabelę w bazie danych. Są to:
- Kategoria – zawiera informacje o kategoriach, takie jak jej nazwa, opis, zdjęcie;
- Konto – informacje dotyczące kont użytkowników, dane personalne i dane logowania;
- Koszyk – dane dotyczące produktów w koszyku;
- Zamowienie – informacje na temat zamówień, ich kosztów, statusów i przypisanych do nich kont;
- LiniaZamowienia – zawiera informacje o produktach wchodzących w skład danego zamówienia;
- Kupon – dane kuponów obniżających cenę zakupów, możliwych do wykorzystania przez klientów.

Szablony stron html znajdują się w folderze „templates”. W projektowaniu wizualnej strony sklepu wykorzystano nieodpłatnie dostępne wzorce ze strony https://htmlcodex.com, bazujące na licencji Creative Commons, które następnie zmodyfikowano i dostosowano do potrzeb sklepu [https://htmlcodex.com/bootstrap-shop-template/](https://htmlcodex.com/bootstrap-shop-template/). Pliki multimedialne, takie jak zdjęcia produktów zapisywane są w folderze „media”.