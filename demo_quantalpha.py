#!/usr/bin/env python3
"""
Script de demonstração do QuantAlpha
Exemplo completo de uso da análise quantitativa
"""

from quantalpha import QuantAlpha
import warnings
warnings.filterwarnings('ignore')

def demonstrar_quantalpha():
    """Demonstração completa do sistema QuantAlpha"""
    
    print("="*80)
    print("🤖 DEMONSTRAÇÃO QUANTALPHA - ANALISTA QUANTITATIVO B3")
    print("="*80)
    
    # Inicializar QuantAlpha
    qa = QuantAlpha()
    
    # Lista de ativos para demonstração
    ativos_demo = ['PETR4', 'VALE3', 'ITUB4']
    
    for ativo in ativos_demo:
        print(f"\n{'='*20} ANÁLISE: {ativo} {'='*20}")
        
        try:
            # Análise técnica completa
            analysis = qa.analyze_asset(ativo)
            
            if 'error' in analysis:
                print(f"❌ Erro na análise: {analysis['error']}")
                continue
            
            # Exibir métricas principais
            print(f"\n📊 MÉTRICAS QUANTITATIVAS:")
            print(f"   💰 Preço Atual: R$ {analysis['current_price']:.2f}")
            print(f"   📈 Taxa de Acerto: {analysis['backtest']['hit_rate']*100:.1f}%")
            print(f"   🎯 Fator de Lucro: {analysis['backtest']['profit_factor']:.2f}")
            print(f"   ⚠️ Drawdown Máximo: {analysis['backtest']['max_drawdown']*100:.1f}%")
            print(f"   🔬 Expectativa Matemática: {analysis['backtest']['expectativa_matematica']*100:.3f}%")
            print(f"   📊 RSI Atual: {analysis['current_rsi']:.1f}")
            
            # Faixas de volatilidade
            vol_ranges = analysis['volatility_ranges']
            print(f"\n📊 FAIXAS DE VOLATILIDADE ESPERADA:")
            print(f"   🎯 68% Prob (1σ): R$ {vol_ranges['lower_1std']:.2f} - R$ {vol_ranges['upper_1std']:.2f}")
            print(f"   🎯 95% Prob (2σ): R$ {vol_ranges['lower_2std']:.2f} - R$ {vol_ranges['upper_2std']:.2f}")
            
            # Níveis técnicos
            tech = analysis['technical_levels']
            print(f"\n🎯 NÍVEIS TÉCNICOS:")
            print(f"   📈 MA20: R$ {tech['ma20']:.2f}")
            print(f"   📉 Suporte: R$ {tech['support']:.2f}")
            print(f"   📈 Resistência: R$ {tech['resistance']:.2f}")
            
            # Avaliação rápida
            print(f"\n🧠 AVALIAÇÃO QUANTALPHA:")
            
            score = 0
            comentarios = []
            
            if analysis['backtest']['hit_rate'] > 0.6:
                score += 2
                comentarios.append("✅ Alta taxa de acerto histórica")
            elif analysis['backtest']['hit_rate'] > 0.5:
                score += 1
                comentarios.append("⚠️ Taxa de acerto moderada")
            else:
                comentarios.append("❌ Taxa de acerto baixa")
            
            if analysis['backtest']['profit_factor'] > 1.5:
                score += 2
                comentarios.append("✅ Fator de lucro robusto")
            elif analysis['backtest']['profit_factor'] > 1.2:
                score += 1
                comentarios.append("⚠️ Fator de lucro moderado")
            else:
                comentarios.append("❌ Fator de lucro insuficiente")
            
            if analysis['backtest']['max_drawdown'] > -0.15:
                score += 2
                comentarios.append("✅ Drawdown controlado")
            elif analysis['backtest']['max_drawdown'] > -0.25:
                score += 1
                comentarios.append("⚠️ Drawdown moderado")
            else:
                comentarios.append("❌ Drawdown elevado")
            
            # Conclusão
            if score >= 5:
                conclusion = "🟢 PERFIL ATRATIVO para estratégias quantitativas"
            elif score >= 3:
                conclusion = "🟡 PERFIL MODERADO - requer análise adicional"
            else:
                conclusion = "🔴 PERFIL DE RISCO ELEVADO"
            
            for comentario in comentarios:
                print(f"   {comentario}")
            
            print(f"\n   📋 CONCLUSÃO: {conclusion}")
            
        except Exception as e:
            print(f"❌ Erro durante análise de {ativo}: {e}")
    
    print(f"\n{'='*80}")
    print("🎯 DEMONSTRAÇÃO CONCLUÍDA")
    print("💡 Para análise completa com relatório detalhado, use:")
    print("   qa.get_quantalpha_prompt_response('TICKER')")
    print("📊 Para interface web interativa, execute:")
    print("   streamlit run app_quantalpha.py")
    print("="*80)

if __name__ == "__main__":
    demonstrar_quantalpha()