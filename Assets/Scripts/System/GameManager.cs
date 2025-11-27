using UnityEngine;
using UnityEngine.UI;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance;
    public static bool gameStarted = false;

    [Header("Fuel Settings")]
    [SerializeField] private Slider fuelSlider;
    public float fuelLimit = 30f; // 이 값은 Start에서 덮어씌워집니다.
    public float currentFuel;
    public float fuelCostPerJump = 2f;

    void Awake()
    {
        // GameManager는 씬 이동 시 파괴되고 새로 만들어지는 것이 관리하기 편합니다.
        // DontDestroyOnLoad 제거됨
        if (Instance == null)
        {
            Instance = this;
        }
        else
        {
            Destroy(gameObject);
        }
    }

    void Start()
    {
        // 1. ScoreManager에서 업그레이드된 연료통 크기 가져오기
        if (ScoreManager.Instance != null)
        {
            fuelLimit = ScoreManager.Instance.MaxFuelLimit;
            // 2. 점수 0점으로 초기화
            ScoreManager.Instance.ResetScore();
        }
        else
        {
            // 혹시라도 바로 PlayScene부터 시작해서 ScoreManager가 없을 경우를 대비한 기본값
            fuelLimit = 30f;
            Debug.LogWarning("ScoreManager를 찾을 수 없습니다. 기본 연료값(30)을 사용합니다.");
        }

        // 3. 가져온 크기만큼 연료 채우기
        ResetFuel();
        UpdateFuelUI();

        //Debug.Log("게임 시작! 적용된 연료통 크기: " + fuelLimit);
    }

    public void ResetFuel()
    {
        currentFuel = fuelLimit;
        UpdateFuelUI();
    }

    public bool UseFuel()
    {
        if (currentFuel >= fuelCostPerJump)
        {
            currentFuel -= fuelCostPerJump;
            UpdateFuelUI();
            return true;
        }
        return false;
    }

    public void AddFuelLimit(float amount)
    {
        // 게임 도중 아이템을 먹어서 '잠시' 늘어나는 경우에만 사용
        fuelLimit += amount;
        currentFuel = fuelLimit;
        UpdateFuelUI();
    }

    public void UpdateFuelUI()
    {
        if (fuelSlider != null)
        {
            fuelSlider.value = currentFuel / fuelLimit;
        }
        // Slider가 자주 없어질 수 있으므로 매번 경고를 띄우지는 않음 (선택사항)
    }

    public void SetFuelSlider(Slider slider)
    {
        fuelSlider = slider;
        UpdateFuelUI();
    }
}