import streamlit as st
import matplotlib.pyplot as plt

# Configuration de la page
st.set_page_config(page_title="Cantine ODD - Vaucluse", page_icon="🍏")

st.title("Cantine ODD : Suivi des Déchets 🍏")
st.write("Collège du Vaucluse - 700 Demi-pensionnaires")

st.markdown("---")

st.subheader("1. Saisie des données du jour (en kg)")

# Les cases de saisie pour l'utilisateur
v_alim = st.number_input("Déchets alimentaires globaux (en kg) :", min_value=0.0, step=0.1, value=0.0)
v_serv = st.number_input("Serviettes en papier (en kg) :", min_value=0.0, step=0.1, value=0.0)
v_pain = st.number_input("Pain gaspillé (en kg) :", min_value=0.0, step=0.1, value=0.0)
v_emb = st.number_input("Emballages (en kg) :", min_value=0.0, step=0.1, value=0.0)
v_fruits = st.number_input("Fruits entamés (en kg) :", min_value=0.0, step=0.1, value=0.0)

if st.button("Calculer le bilan", type="primary"):
    total = v_alim + v_serv + v_pain + v_emb + v_fruits
    
    if total == 0:
        st.error("Ajoute des kilos dans les cases avant de calculer !")
    else:
        st.markdown("---")
        st.subheader("📊 Résultats du jour :")
        
        # Calcul de la moyenne pour 700 élèves (en grammes)
        moyenne_g = (total * 1000) / 700
        
        st.metric(label="Poids Total des Déchets", value=f"{total:.1f} kg")
        st.metric(label="Moyenne par élève", value=f"{moyenne_g:.1f} g / élève")
        
        # Calcul des pourcentages
        p_alim = (v_alim / total) * 100
        p_serv = (v_serv / total) * 100
        p_pain = (v_pain / total) * 100
        p_emb = (v_emb / total) * 100
        p_fruits = (v_fruits / total) * 100
        
        st.write("#### Répartition :")
        st.write(f"- Déchets alimentaires : **{p_alim:.1f}%** ({v_alim} kg)")
        st.write(f"- Serviettes papier : **{p_serv:.1f}%** ({v_serv} kg)")
        st.write(f"- Pain : **{p_pain:.1f}%** ({v_pain} kg)")
        st.write(f"- Emballages : **{p_emb:.1f}%** ({v_emb} kg)")
        st.write(f"- Fruits entamés : **{p_fruits:.1f}%** ({v_fruits} kg)")
        
        # Création du graphique en camembert avec Matplotlib
        labels = ['Alimentaire', 'Serviettes', 'Pain', 'Emballages', 'Fruits']
        sizes = [v_alim, v_serv, v_pain, v_emb, v_fruits]
        colors = ['#ff9800', '#9e9e9e', '#8d6e63', '#2196f3', '#4caf50']
        
        # On ne garde pour le graphique que les sections qui ne sont pas à 0
        labels_filtres = [l for l, s in zip(labels, sizes) if s > 0]
        sizes_filtres = [s for s in sizes if s > 0]
        colors_filtres = [c for c, s in zip(colors, sizes) if s > 0]
        
        fig, ax = plt.subplots()
        ax.pie(sizes_filtres, labels=labels_filtres, autopct='%1.1f%%', startangle=90, colors=colors_filtres)
        ax.axis('equal')  # Pour que le camembert soit bien rond
        
        # Affichage du graphique dans Streamlit
        st.pyplot(fig)
