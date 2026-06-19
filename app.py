<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welf.io</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Arial, sans-serif;
        }

        body{
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            background:linear-gradient(135deg, #0f172a, #1e293b);
        }

        .window{
            width:500px;
            background:white;
            border-radius:15px;
            overflow:hidden;
            box-shadow:0 10px 30px rgba(0,0,0,0.3);
        }

        .window-header{
            background:#f1f5f9;
            padding:12px;
            display:flex;
            gap:8px;
        }

        .dot{
            width:12px;
            height:12px;
            border-radius:50%;
        }

        .red{background:#ff5f57;}
        .yellow{background:#ffbd2e;}
        .green{background:#28c840;}

        .content{
            padding:50px;
            text-align:center;
        }

        h1{
            color:#0f172a;
            font-size:48px;
            margin-bottom:15px;
        }

        p{
            color:#64748b;
            margin-bottom:25px;
        }

        button{
            padding:12px 25px;
            border:none;
            border-radius:8px;
            background:#2563eb;
            color:white;
            cursor:pointer;
            font-size:16px;
        }

        button:hover{
            background:#1d4ed8;
        }
    </style>
</head>
<body>

    <div class="window">
        <div class="window-header">
            <div class="dot red"></div>
            <div class="dot yellow"></div>
            <div class="dot green"></div>
        </div>

        <div class="content">
            <h1>Welf.io</h1>
            <p>Bienvenue sur la plateforme Welf.io</p>
            <button>Commencer</button>
        </div>
    </div>

</body>
</html>
