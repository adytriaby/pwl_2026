<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PageController extends Controller
{
    public function index()
    {
        return 'Selamat Datang';
    }

    public function about()
    {
        return 'Nama: Yab | NIM: 2341720000';
    }

    public function articles($id)
    {
        return 'Halaman Artikel dengan ID '.$id;
    }
}
