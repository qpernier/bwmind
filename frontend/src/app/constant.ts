export class Urls{
    private static baseUrl: string = 'http://127.0.0.1:8000/api/';
    public static ias: string = Urls.baseUrl + 'ias';
    public static newGame: string = Urls.baseUrl + 'newgame?iaCode=';
    public static play:string = Urls.baseUrl + 'play';
}

export class Constant{
    /**Square size in px */
    public static squareSize:number = 100;
    /**Pawn size in px */
    public static pawnSize:number = 65;
}