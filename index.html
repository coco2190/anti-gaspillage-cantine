<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Suivi des Déchets - Collège du Vaucluse</title>
    <!-- Chargement sécurisé de la bibliothèque pour le graphique -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            padding: 20px;
        }
        .boite-principale {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #ddd;
        }
        h1 { color: #2e7d32; text-align: center; }
        .poubelle { margin-bottom: 12px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input { width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; }
        button { width: 100%; background: #2e7d32; color: white; padding: 10px; border: none; border-radius: 4px; font-size: 16px; cursor: pointer; margin-top: 10px; font-weight: bold; }
        button:hover { background: #1b5e20; }
        .resultats { background: #e8f5e9; padding: 15px; margin-top: 20px; border-radius: 6px; display: none; }
        .espace-camembert { width: 250px; height: 250px; margin: 20px auto 0 auto; }
    </style>
</head>
<body>

<div class="boite-principale">
    <h1>Cantine ODD : Suivi des Déchets 🍏</h1>
    <p style="text-align:center;">Collège du Vaucluse - 700 Demi-pensionnaires</p>
    
    <hr>
    
    <div class="poubelle">
        <label>1. Déchets alimentaires globaux (en kg) :</label>
        <input type="number" id="inputAlim" step="0.1" value="0">
    </div>
    <div class="poubelle">
        <label>2. Serviettes en papier (en kg) :</label>
        <input type="number" id="inputServiettes" step="0.1" value="0">
    </div>
    <div class="poubelle">
        <label>3. Pain gaspillé (en kg) :</label>
        <input type="number" id="inputPain" step="0.1" value="0">
    </div>
    <div class="poubelle">
        <label>4. Emballages (en kg) :</label>
        <input type="number" id="inputEmballages" step="0.1" value="0">
    </div>
    <div class="poubelle">
        <label>5. Fruits entamés (en kg) :</label>
        <input type="number" id="inputFruits" step="0.1" value="0">
    </div>
    
    <button onclick="faireLesCalculs()">Calculer le bilan</button>
    
    <!-- Zone d'affichage des résultats -->
    <div id="blocResultats" class="resultats">
        <h3>📊 Résultats du jour :</h3>
        <p><b>Poids Total :</b> <span id="txtTotal">0</span> kg</p>
        <p><b>Moyenne par élève :</b> <span id="txtMoyenne">0</span> g / élève</p>
        
        <h4>Répartition :</h4>
        <ul>
            <li>Déchets alimentaires : <span id="pctAlim">0</span>%</li>
            <li>Serviettes papier : <span id="pctServiettes">0</span>%</li>
            <li>Pain : <span id="pctPain">0</span>%</li>
            <li>Emballages : <span id="pctEmballages">0</span>%</li>
            <li>Fruits entamés : <span id="pctFruits">0</span>%</li>
        </ul>
        
        <div class="espace-camembert">
            <canvas id="graphiqueCamembert"></canvas>
        </div>
    </div>
</div>

<script>
let monGraphique = null;

function faireLesCalculs() {
    // Récupération des données
    let vAlim = parseFloat(document.getElementById('inputAlim').value) || 0;
    let vServ = parseFloat(document.getElementById('inputServiettes').value) || 0;
    let vPain = parseFloat(document.getElementById('inputPain').value) || 0;
    let vEmb = parseFloat(document.getElementById('inputEmballages').value) || 0;
    let vFru = parseFloat(document.getElementById('inputFruits').value) || 0;
    
    let total = vAlim + vServ + vPain + vEmb + vFru;
    
    if(total === 0) {
        alert("Ajoute des kilos dans les cases avant de calculer !");
        return;
    }
    
    // Moyenne pour 700 élèves (en grammes)
    let moyenneG = ((total * 1000) / 700).toFixed(1);
    
    // Affichage des chiffres et pourcentages
    document.getElementById('txtTotal').innerText = total.toFixed(1);
    document.getElementById('txtMoyenne').innerText = moyenneG;
    
    document.getElementById('pctAlim').innerText = ((vAlim / total) * 100).toFixed(1);
    document.getElementById('pctServiettes').innerText = ((vServ / total) * 100).toFixed(1);
    document.getElementById('pctPain').innerText = ((vPain / total) * 100).toFixed(1);
    document.getElementById('pctEmballages').innerText = ((vEmb / total) * 100).toFixed(1);
    document.getElementById('pctFruits').innerText = ((vFru / total) * 100).toFixed(1);
    
    // Rendre la zone visible
    document.getElementById('blocResultats').style.display = 'block';
    
    // Création du camembert
    let ctx = document.getElementById('graphiqueCamembert').getContext('2d');
    if (monGraphique !== null) { monGraphique.destroy(); }
    
    monGraphique = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Alimentaire', 'Serviettes', 'Pain', 'Emballages', 'Fruits'],
            datasets: [{
                data: [vAlim, vServ, vPain, vEmb, vFru],
                backgroundColor: ['#ff9800', '#9e9e9e', '#8d6e63', '#2196f3', '#4caf50']
            }]
        },
        options: { responsive: true, maintainAspectRatio: false }
    });
}
</script>

</body>
</html>
