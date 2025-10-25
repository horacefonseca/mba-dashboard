"""
Market Basket Analysis Interactive Dashboard
Educational Data Mining Assignment - MBA with Apriori

Dataset: The Bread Basket (Edinburgh Bakery)
Author: Emmanuel
Date: 2025-10-23
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import networkx as nx

# Page configuration
st.set_page_config(
    page_title="Market Basket Analysis Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Load data with caching
@st.cache_data
def load_data():
    """Load all CSV data files"""
    try:
        rules = pd.read_csv("data/pbi_association_rules.csv")
        items = pd.read_csv("data/pbi_item_frequencies.csv")
        stats_raw = pd.read_csv("data/pbi_transaction_statistics.csv")
        network = pd.read_csv("data/pbi_item_pairs_network.csv")

        # Rename columns to standard format if needed
        if 'IF Customer Buys' in rules.columns:
            rules = rules.rename(columns={
                'IF Customer Buys': 'antecedents',
                'THEN Also Buys': 'consequents',
                'Support': 'support',
                'Confidence': 'confidence',
                'Lift': 'lift',
                'Leverage': 'leverage',
                'Conviction': 'conviction'
            })

        # Transform stats from long to wide format
        if 'Metric' in stats_raw.columns:
            # Create a dictionary for easy access
            stats_dict = dict(zip(stats_raw['Metric'], stats_raw['Value']))
            # Convert to DataFrame with standard column names
            stats = pd.DataFrame([{
                'total_transactions': stats_dict.get('Total Transactions', 0),
                'avg_basket_size': stats_dict.get('Average Basket Size', 0),
                'unique_items': stats_dict.get('Total Items (Unique)', 0)
            }])
        else:
            stats = stats_raw

        return rules, items, stats, network
    except FileNotFoundError as e:
        st.error(f"Error loading data files: {e}")
        st.stop()

# Load data
rules_df, items_df, stats_df, network_df = load_data()

# Main title
st.markdown('<h1 class="main-header">🛒 Market Basket Analysis Dashboard</h1>', unsafe_allow_html=True)
st.markdown("**The Bread Basket Dataset** - Edinburgh Bakery Transaction Analysis (Oct-Dec 2016)")
st.markdown("---")

# Sidebar - Filters
st.sidebar.header("🔍 Filter Controls")
st.sidebar.markdown("Adjust thresholds to explore association rules:")

# Support filter
min_support = st.sidebar.slider(
    "Minimum Support (%)",
    min_value=0.0,
    max_value=30.0,
    value=3.0,
    step=0.5,
    help="Percentage of transactions containing the itemset"
)

# Confidence filter
min_confidence = st.sidebar.slider(
    "Minimum Confidence (%)",
    min_value=0.0,
    max_value=100.0,
    value=50.0,
    step=5.0,
    help="Probability of consequent given antecedent"
)

# Lift filter
min_lift = st.sidebar.slider(
    "Minimum Lift",
    min_value=1.0,
    max_value=5.0,
    value=1.0,
    step=0.1,
    help="Correlation strength (>1 = positive association)"
)

# Search functionality
st.sidebar.markdown("---")
st.sidebar.subheader("🔎 Search Items")
search_term = st.sidebar.text_input(
    "Search for specific item:",
    placeholder="e.g., Coffee, Bread"
)

# Filter data based on sliders
filtered_rules = rules_df[
    (rules_df['support'] >= min_support / 100) &
    (rules_df['confidence'] >= min_confidence / 100) &
    (rules_df['lift'] >= min_lift)
].copy()

# Apply search filter if search term exists
if search_term:
    filtered_rules = filtered_rules[
        filtered_rules['antecedents'].str.contains(search_term, case=False, na=False) |
        filtered_rules['consequents'].str.contains(search_term, case=False, na=False)
    ]

# Sort by lift (descending)
filtered_rules = filtered_rules.sort_values('lift', ascending=False)

# Display statistics
st.sidebar.markdown("---")
st.sidebar.subheader("📊 Dataset Statistics")
st.sidebar.metric("Total Transactions", f"{stats_df['total_transactions'].values[0]:,}")
st.sidebar.metric("Avg Basket Size", f"{stats_df['avg_basket_size'].values[0]:.2f}")
st.sidebar.metric("Unique Items", f"{stats_df['unique_items'].values[0]:,}")
st.sidebar.metric("Rules Found", len(filtered_rules))

# Main content area
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📋 Total Rules",
        value=len(rules_df),
        delta=f"{len(filtered_rules)} after filtering"
    )

with col2:
    if len(filtered_rules) > 0:
        avg_support = filtered_rules['support'].mean() * 100
        st.metric(
            label="📊 Avg Support",
            value=f"{avg_support:.1f}%"
        )
    else:
        st.metric(label="📊 Avg Support", value="N/A")

with col3:
    if len(filtered_rules) > 0:
        avg_confidence = filtered_rules['confidence'].mean() * 100
        st.metric(
            label="🎯 Avg Confidence",
            value=f"{avg_confidence:.1f}%"
        )
    else:
        st.metric(label="🎯 Avg Confidence", value="N/A")

with col4:
    if len(filtered_rules) > 0:
        max_lift = filtered_rules['lift'].max()
        st.metric(
            label="🚀 Max Lift",
            value=f"{max_lift:.2f}"
        )
    else:
        st.metric(label="🚀 Max Lift", value="N/A")

st.markdown("---")

# Check if any rules match filters
if len(filtered_rules) == 0:
    st.warning("⚠️ No rules match the current filters. Try adjusting the thresholds.")
else:
    # Tab layout for different views
    tab1, tab2, tab3 = st.tabs(["📋 Association Rules", "📊 Visualizations", "🕸️ Network Graph"])

    with tab1:
        st.subheader("Association Rules Table")
        st.markdown(f"Showing **{len(filtered_rules)}** rules matching your criteria")

        # Format the dataframe for display
        display_df = filtered_rules.copy()
        display_df['support'] = (display_df['support'] * 100).round(2).astype(str) + '%'
        display_df['confidence'] = (display_df['confidence'] * 100).round(2).astype(str) + '%'
        display_df['lift'] = display_df['lift'].round(2)
        display_df['leverage'] = display_df['leverage'].round(4)
        display_df['conviction'] = display_df['conviction'].round(2)

        # Rename columns for better display
        display_df = display_df.rename(columns={
            'antecedents': 'If Customer Buys',
            'consequents': 'Then Also Buys',
            'support': 'Support',
            'confidence': 'Confidence',
            'lift': 'Lift',
            'leverage': 'Leverage',
            'conviction': 'Conviction'
        })

        # Display top 20 rules
        st.dataframe(
            display_df.head(20),
            use_container_width=True,
            hide_index=True
        )

        # Download button for filtered rules
        csv = filtered_rules.to_csv(index=False)
        st.download_button(
            label="📥 Download Filtered Rules (CSV)",
            data=csv,
            file_name="filtered_association_rules.csv",
            mime="text/csv"
        )

        # Business interpretation
        st.markdown("---")
        st.subheader("💡 Top 5 Recommendations")

        for idx, row in filtered_rules.head(5).iterrows():
            with st.expander(f"#{idx+1}: {row['antecedents']} → {row['consequents']}"):
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown(f"**Metrics:**")
                    st.markdown(f"- Support: {row['support']*100:.1f}%")
                    st.markdown(f"- Confidence: {row['confidence']*100:.1f}%")
                    st.markdown(f"- Lift: {row['lift']:.2f}")
                with col_b:
                    st.markdown(f"**Business Insight:**")
                    st.markdown(f"When customers buy **{row['antecedents']}**, they have a **{row['confidence']*100:.1f}%** chance of also buying **{row['consequents']}**.")
                    st.markdown(f"This pairing is **{row['lift']:.2f}x** more likely than random chance.")

    with tab2:
        st.subheader("Association Metrics Visualizations")

        # Create 2x2 subplot grid
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=(
                'Support vs Confidence (colored by Lift)',
                'Distribution of Lift',
                'Distribution of Confidence',
                'Lift vs Leverage'
            ),
            specs=[
                [{"type": "scatter"}, {"type": "histogram"}],
                [{"type": "histogram"}, {"type": "scatter"}]
            ]
        )

        # 1. Support vs Confidence scatter (colored by Lift)
        fig.add_trace(
            go.Scatter(
                x=filtered_rules['support'] * 100,
                y=filtered_rules['confidence'] * 100,
                mode='markers',
                marker=dict(
                    size=8,
                    color=filtered_rules['lift'],
                    colorscale='Viridis',
                    showscale=True,
                    colorbar=dict(title="Lift", x=0.46)
                ),
                text=[f"{a} → {c}" for a, c in zip(filtered_rules['antecedents'], filtered_rules['consequents'])],
                hovertemplate='<b>%{text}</b><br>Support: %{x:.1f}%<br>Confidence: %{y:.1f}%<extra></extra>',
                showlegend=False
            ),
            row=1, col=1
        )

        # 2. Distribution of Lift
        fig.add_trace(
            go.Histogram(
                x=filtered_rules['lift'],
                nbinsx=20,
                marker_color='skyblue',
                showlegend=False
            ),
            row=1, col=2
        )

        # 3. Distribution of Confidence
        fig.add_trace(
            go.Histogram(
                x=filtered_rules['confidence'] * 100,
                nbinsx=20,
                marker_color='lightcoral',
                showlegend=False
            ),
            row=2, col=1
        )

        # 4. Lift vs Leverage scatter
        fig.add_trace(
            go.Scatter(
                x=filtered_rules['lift'],
                y=filtered_rules['leverage'],
                mode='markers',
                marker=dict(size=8, color='green', opacity=0.6),
                text=[f"{a} → {c}" for a, c in zip(filtered_rules['antecedents'], filtered_rules['consequents'])],
                hovertemplate='<b>%{text}</b><br>Lift: %{x:.2f}<br>Leverage: %{y:.4f}<extra></extra>',
                showlegend=False
            ),
            row=2, col=2
        )

        # Update axes labels
        fig.update_xaxes(title_text="Support (%)", row=1, col=1)
        fig.update_yaxes(title_text="Confidence (%)", row=1, col=1)
        fig.update_xaxes(title_text="Lift", row=1, col=2)
        fig.update_yaxes(title_text="Frequency", row=1, col=2)
        fig.update_xaxes(title_text="Confidence (%)", row=2, col=1)
        fig.update_yaxes(title_text="Frequency", row=2, col=1)
        fig.update_xaxes(title_text="Lift", row=2, col=2)
        fig.update_yaxes(title_text="Leverage", row=2, col=2)

        # Update layout
        fig.update_layout(height=700, showlegend=False)

        st.plotly_chart(fig, use_container_width=True)

        # Top 10 rules bar chart
        st.markdown("---")
        st.subheader("Top 10 Association Rules by Lift")

        top_10 = filtered_rules.head(10).copy()
        top_10['rule'] = top_10['antecedents'] + ' → ' + top_10['consequents']

        fig_bar = px.bar(
            top_10,
            x='lift',
            y='rule',
            orientation='h',
            color='lift',
            color_continuous_scale='Blues',
            labels={'lift': 'Lift', 'rule': 'Association Rule'},
            hover_data={
                'support': ':.2%',
                'confidence': ':.2%',
                'lift': ':.2f'
            }
        )
        fig_bar.update_layout(
            height=400,
            yaxis={'categoryorder': 'total ascending'},
            showlegend=False
        )

        st.plotly_chart(fig_bar, use_container_width=True)

    with tab3:
        st.subheader("Association Network Graph")
        st.markdown("Visualizing item relationships as an interactive network")

        # Create network graph
        G = nx.Graph()

        # Add edges from filtered rules (limit to top 15 for clarity)
        top_rules = filtered_rules.head(15)
        for _, row in top_rules.iterrows():
            G.add_edge(
                row['antecedents'],
                row['consequents'],
                weight=row['lift'],
                support=row['support'],
                confidence=row['confidence']
            )

        # Get positions using spring layout
        pos = nx.spring_layout(G, k=2, iterations=50)

        # Create edge trace
        edge_trace = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_data = G.get_edge_data(edge[0], edge[1])

            edge_trace.append(
                go.Scatter(
                    x=[x0, x1, None],
                    y=[y0, y1, None],
                    mode='lines',
                    line=dict(width=edge_data['weight'], color='lightgray'),
                    hoverinfo='none',
                    showlegend=False
                )
            )

        # Create node trace
        node_x = []
        node_y = []
        node_text = []
        node_size = []

        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            node_text.append(node)
            # Size based on degree (number of connections)
            node_size.append(G.degree(node) * 10 + 20)

        node_trace = go.Scatter(
            x=node_x,
            y=node_y,
            mode='markers+text',
            text=node_text,
            textposition='top center',
            marker=dict(
                size=node_size,
                color='lightblue',
                line=dict(color='darkblue', width=2)
            ),
            hovertemplate='<b>%{text}</b><br>Connections: %{marker.size}<extra></extra>',
            showlegend=False
        )

        # Create figure
        fig_network = go.Figure(data=edge_trace + [node_trace])
        fig_network.update_layout(
            showlegend=False,
            hovermode='closest',
            margin=dict(b=0, l=0, r=0, t=0),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=600,
            plot_bgcolor='white'
        )

        st.plotly_chart(fig_network, use_container_width=True)

        st.info("💡 **Tip:** Node size represents the number of connections. Larger nodes are 'hub' products that pair well with many items.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Market Basket Analysis Dashboard | Data Mining Assignment | The Bread Basket Dataset (Oct-Dec 2016)</p>
    <p>Built with Streamlit & Plotly | Apriori Algorithm via mlxtend</p>
</div>
""", unsafe_allow_html=True)
