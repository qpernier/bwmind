export class Urls{
    private static baseUrl: string = 'http://127.0.0.1:8000/api/';
    public static ias: string = Urls.baseUrl + 'ias';
    public static newGame: string = Urls.baseUrl + '/newgame?iaCode=';
}